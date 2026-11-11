#internet speed

# Checking internet speed

try:
    import speedtest
except ModuleNotFoundError:
    raise SystemExit("The 'speedtest' package is missing. Install it with: pip install speedtest-cli")


def main() -> None:
    st = speedtest.Speedtest()
    st.get_best_server()

    download = st.download() / 1_000_000
    upload = st.upload() / 1_000_000
    ping = st.results.ping

    print(f"Download: {download:.2f} Mbps")
    print(f"Upload: {upload:.2f} Mbps")
    print(f"Ping: {ping:.2f} ms")


if __name__ == "__main__":
    main()