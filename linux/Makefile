PREFIX ?= /usr/local
BINDIR = $(DESTDIR)$(PREFIX)/bin/
MANDIR = $(DESTDIR)$(PREFIX)/share/man/man1
DOCDIR = $(DESTDIR)$(PREFIX)/share/doc/docbao

.PHONY: all install uninstall 

all:

install:
	install -m755 -d $(BINDIR)
	install -m755 -d $(MANDIR)
	install -m755 -d $(DOCDIR)
	install -m755 docbao $(BINDIR)
	install -m755 utility.py $(BINDIR)
	install -m644 help.txt $(DOCDIR)

uninstall:
	rm -f $(BINDIR)/docbao
	rm -f $(BINDIR)/utility.py
	rm -rf $(BINDIR)/data
	rm -rf $(BINDIR)/export
	rm -rf $(DOCDIR)
