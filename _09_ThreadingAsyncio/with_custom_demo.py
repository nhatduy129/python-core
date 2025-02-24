class DemoContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        
with DemoContextManager() as demo:
    print("Inside the context")
