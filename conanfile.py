from conans import ConanFile

class BotanConan(ConanFile):
    name = "Botan"
    version = "2.1.0"
    settings = "os", "compiler", "build_type", "arch"
    description = "Package for Botan"
    url = "None"
    license = "None"

    def package_info(self):
	self.cpp_info.includedirs = ['include']  # Ordered list of include paths
	self.cpp_info.libdirs = ['obj/lib']  # Directories where libraries can be found
