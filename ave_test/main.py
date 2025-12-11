import uvicorn

from ave_test.bootstrap import build_app


application = build_app()

def main():
    uvicorn.run(application)

if __name__ == "__main__":
    main()
