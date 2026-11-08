from src.config_libraries import required, check, check_missing, install_missing

def main():
    required()
    check()
    check_missing()
    install_missing()

if __name__ == "__main__":
    main()