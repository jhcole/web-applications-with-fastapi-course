import fastapi
import fastapi_chameleon
import uvicorn
from starlette.staticfiles import StaticFiles

from views import home
from views import account
from views import packages

app = fastapi.FastAPI()


def main():
    print("Running in dev mode. Use `uvicorn main:app` to run in production.")
    configure(dev_mode=True)
    uvicorn.run(
        "main:app", host="127.0.0.1", port=8000, reload=True, reload_includes="*.pt"
    )


def configure(dev_mode: bool):
    configure_templates(dev_mode)
    configure_routes()


def configure_templates(dev_mode: bool):
    fastapi_chameleon.global_init("templates", auto_reload=dev_mode)


def configure_routes():
    app.mount("/static", StaticFiles(directory="static"))
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == "__main__":
    main()
else:
    # Production
    configure(dev_mode=False)
