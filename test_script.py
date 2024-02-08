if __name__ == "__main__":
    import dvc.api
    from dvclive import Live

    params = dvc.api.params_show()
    with Live() as live:
        live.log_param("parameter", params["x"])