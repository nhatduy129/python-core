## 1. transaction.atomic() and select_for_update
### a. transaction.atomic có 2 loại là `@transaction.atomic` và `with transaction.atomic()`. Ví dụ 2 code bên dưới là hoàn toàn tương đương nhau.

```python
    @transaction.atomic
    def add_balance(self, amount: int):
        user = NormalUser.objects.select_for_update().get(id=self.id)  # lock row if there are multiple threads with same user.id
        user._balance += amount
        user.save(update_fields=["_balance"])  # commit transaction, unlock row
```

```python
def add_balance(user_id, amount):
    with transaction.atomic():
        user = NormalUser.objects.select_for_update().get(id=self.id) # bắt đầu lock row
        user.balance += amount
        user.save() # commit transaction, unlock row
```
`with transaction.atomic()` được dùng khi trong hàm còn có những dòng code khác cần bỏ bên ngoài block transaction.atomic.  
Nếu toàn bộ code đều nằm trong block transaction.atomic thì không cần thiết phải dùng nó, dùng `@transaction.atomic` clean code hơn.
### b. select_for_update
`select_for_update` là một phương thức của Django ORM, nó sẽ lock row trong khi transaction đang chạy. Sẽ unlock khi ra khỏi block code của `with transaction.atomic()`.

### c. Lưu ý
- `select_for_update` sẽ lock row nhưng chỉ lock bên trong block code của `with transaction.atomic()`. Do đó nếu có nhiều hàm cùng thực thi thì sẽ không lock được row.
Ví dụ
```python
    @transaction.atomic
    def add_balance(self, amount: int):
        user = GoodUser.objects.select_for_update().get(id=self.id)
        user._balance += amount
        user.save(update_fields=["_balance"])
        
    @transaction.atomic
    def reduce_balance(self, amount: int):
        user = GoodUser.objects.select_for_update().get(id=self.id)
        if user._balance >= amount:
            user._balance -= amount
            user.save(update_fields=["_balance"])
        else:
            raise ValueError("Not enough balance")
```
Cả 2 hàm trên, nếu có nhiều threads cùng gọi xen kẽ nhau thì sẽ không lock được row -> Race condition sẽ xảy ra.  
Tất nhiên, nếu có nhiều threads cùng gọi 1 hàm thì sẽ lock được row -> Không xảy ra race condition.

- `user = NormalUser.objects.select_for_update().get(id=self.id)` và `user = NormalUser.objects.filter(id=self.id).select_for_update().first()` là giống i chang nhau về mặt solve race condition. Chỉ khác nhau cơ bản ở chỗ `.get(id=self.id)` sẽ raise error nếu không tìm thấy row, `.first()` sẽ không raise error và trả về None.
## 2. F expression
`F expression` là một phương thức của Django ORM, nó sẽ thực thi SQL expression trong database.  
Mọi UPDATE SQL query trong database đều được xử lý tuần tự khi dùng chung 1 row, nếu có nhiều query cùng thực thi thì sẽ chờ query trước kết thúc mới thực thi query tiếp theo. Database nào cũng vậy, bất kể là SQLite, MySQL, PostgreSQL, ...
F expression bản chất là chạy 1 UPDATE query trong database, do đó nó sẽ giải quyét được race condition.
Ví dụ:
```python
    def add_balance(self, amount: int):
        GoodUser.objects.filter(id=self.id).update(_balance=F("_balance") + amount)
        
    def reduce_balance(self, amount: int):
        updated_rows = GoodUser.objects.filter(id=self.id, _balance__gte=amount).update(
            _balance=F("_balance") - amount
        )
        if updated_rows == 0:
            raise ValueError("Not enough balance")
```
Khi dùng `F expression`, Django ORM sẽ chạy UPDATE query trong database và các UPDATE query này sẽ chờ lẫn nhau nếu cùng dùng chung 1 row, do đó sẽ giải quyết được race condition.

## 3. Kiểm chứng
Trong file `demoapp/models.py`, có 2 model `BadUser` và `GoodUser`.  