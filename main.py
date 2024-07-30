from pygd import PyGD

pygd_instance = PyGD()

pygd_instance.load_save("CCLocalLevels.dat")

pygd_instance.write_to_file("CCLocalLevelsDecrypted.xml")

levels = pygd_instance.get_levels()

print(levels)
