%define name pyvorbis
%define version 1.3
%define release %mkrel 8
%define pyoggversion 1.3

Summary: A wrapper for the Vorbis libraries
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ekyo.nerim.net/software/pyogg/%{name}-%{version}.tar.bz2
#gw from Debian: fix Unicode in VorbisComment, add pyao support to the example
Patch: pyvorbis-1.3-unicode.patch
Patch1: pyvorbis-1.3-python2.5.patch
License: LGPL
Group: Development/Python
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libvorbis-devel
BuildRequires: libpython-devel
BuildRequires: pyogg >= %pyoggversion
Requires: pyogg >= %pyoggversion
Url: http://ekyo.nerim.net/software/pyogg/index.html

%description
pyvorbis - a Python wrapper for the Ogg/Vorbis library

Ogg/Vorbis is available at http://www.xiph.org

This is the Vorbis module. You will need to download and install the
Python ogg module (available wherever you got this) before you can
build the vorbis module.


%prep
%setup -q
%patch -p1 -b .unicode
%patch1 -p1 -b .python2.5

%build
python config_unix.py
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS
%py_platsitedir/*


