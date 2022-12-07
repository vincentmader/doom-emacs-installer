install:
	cd ./bin && ./install_emacs
uninstall:
	cd ./bin && ./uninstall_emacs
reinstall:
	make uninstall
	make install
