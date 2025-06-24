from prefect import flow

@flow(log_prints=True)
def say_hello(name:str):
    print(f"Hello {name}!")

if __name__ == "__main__":
    say_hello.serve(name="World")
