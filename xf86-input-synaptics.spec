#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE23B7E70B467F0BF (office@who-t.net)
#
Name     : xf86-input-synaptics
Version  : 1.9.1
Release  : 33
URL      : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-1.9.1.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-1.9.1.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/driver/xf86-input-synaptics-1.9.1.tar.gz.sig
Summary  : X.Org synaptics input driver.
Group    : Development/Tools
License  : MIT
Requires: xf86-input-synaptics-bin = %{version}-%{release}
Requires: xf86-input-synaptics-data = %{version}-%{release}
Requires: xf86-input-synaptics-lib = %{version}-%{release}
Requires: xf86-input-synaptics-license = %{version}-%{release}
Requires: xf86-input-synaptics-man = %{version}-%{release}
BuildRequires : pkgconfig(inputproto)
BuildRequires : pkgconfig(libevdev)
BuildRequires : pkgconfig(recordproto)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xorg-server)
BuildRequires : pkgconfig(xproto)
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
Requires: xf86-input-synaptics-data = %{version}-%{release}
Requires: xf86-input-synaptics-license = %{version}-%{release}
Requires: xf86-input-synaptics-man = %{version}-%{release}

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
Requires: xf86-input-synaptics-lib = %{version}-%{release}
Requires: xf86-input-synaptics-bin = %{version}-%{release}
Requires: xf86-input-synaptics-data = %{version}-%{release}
Provides: xf86-input-synaptics-devel = %{version}-%{release}

%description dev
dev components for the xf86-input-synaptics package.


%package lib
Summary: lib components for the xf86-input-synaptics package.
Group: Libraries
Requires: xf86-input-synaptics-data = %{version}-%{release}
Requires: xf86-input-synaptics-license = %{version}-%{release}

%description lib
lib components for the xf86-input-synaptics package.


%package license
Summary: license components for the xf86-input-synaptics package.
Group: Default

%description license
license components for the xf86-input-synaptics package.


%package man
Summary: man components for the xf86-input-synaptics package.
Group: Default

%description man
man components for the xf86-input-synaptics package.


%prep
%setup -q -n xf86-input-synaptics-1.9.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542110408
export CFLAGS="-O3 -g -fopt-info-vec "
unset LDFLAGS
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1542110408
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/xf86-input-synaptics
cp COPYING %{buildroot}/usr/share/package-licenses/xf86-input-synaptics/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/synclient
/usr/bin/syndaemon

%files data
%defattr(-,root,root,-)
/usr/share/X11/xorg.conf.d/70-synaptics.conf

%files dev
%defattr(-,root,root,-)
/usr/include/xorg/synaptics-properties.h
/usr/lib64/pkgconfig/xorg-synaptics.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/xorg/modules/input/synaptics_drv.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/xf86-input-synaptics/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/synclient.1
/usr/share/man/man1/syndaemon.1
/usr/share/man/man4/synaptics.4
