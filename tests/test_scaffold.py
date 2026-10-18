def test_application_package_can_be_imported():
    import app

    assert app.__name__ == "app"
