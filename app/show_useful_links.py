from colorama import Fore, Style

print(
    Fore.GREEN
    + "INFO"
    + Style.RESET_ALL
    + ":     Swagger "
    + Fore.CYAN
    + "http://127.0.0.1:8000/docs"
)

print(
    Fore.GREEN
    + "INFO"
    + Style.RESET_ALL
    + ":     Kibana "
    + Fore.CYAN
    + "http://localhost:5601/app/dev_tools#/console"
)
