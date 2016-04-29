#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : xf86-input-synaptics
Version  : 1.8.3
Release  : 16
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-1.8.3.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-1.8.3.tar.gz
Summary  : X.Org synaptics input driver.
Group    : Development/Tools
License  : MIT
Requires: xf86-input-synaptics-bin
Requires: xf86-input-synaptics-lib
Requires: xf86-input-synaptics-data
Requires: xf86-input-synaptics-doc
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(recordproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xtst)

%description
Synaptics touchpad driver for X.Org
-----------------------------------
FAQ
---
* Is this free software?

%package bin
Summary: bin components for the xf86-input-synaptics package.
Group: Binaries
Requires: xf86-input-synaptics-data

%description bin
bin components for the xf86-input-synaptics package.


%package data
Summary: data components for the xf86-input-synaptics package.
Group: Data

%description data
data components for the xf86-input-synaptics package.


%package dev
Summary: dev components for the xf86-input-synaptics package.
Group: Development
Requires: xf86-input-synaptics-lib
Requires: xf86-input-synaptics-bin
Requires: xf86-input-synaptics-data
Provides: xf86-input-synaptics-devel

%description dev
dev components for the xf86-input-synaptics package.


%package doc
Summary: doc components for the xf86-input-synaptics package.
Group: Documentation

%description doc
doc components for the xf86-input-synaptics package.


%package lib
Summary: lib components for the xf86-input-synaptics package.
Group: Libraries
Requires: xf86-input-synaptics-data

%description lib
lib components for the xf86-input-synaptics package.


%prep
%setup -q -n xf86-input-synaptics-1.8.3

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/synclient
/usr/bin/syndaemon

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/50-synaptics.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/synaptics-properties.h
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man4/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/synaptics_drv.so
