%define prerel a
%define pyoggversion 1.3

Summary: A wrapper for the Vorbis libraries
Name: pyvorbis
Version: 1.5
Release: %mkrel 0.%prerel.5
Source0: http://ekyo.nerim.net/software/pyogg/%{name}-%{version}%{prerel}.tar.gz
#gw from Debian: fix Unicode in VorbisComment, add pyao support to the example
Patch0: pyvorbis-1.3-unicode.patch
Patch1: pyvorbis-1.5a-python2.5.patch
# fix linking with libogg
Patch2: pyvorbis-1.5a-fix_linking.patch
License: LGPL
Group: Development/Python
BuildRequires: pkgconfig(vorbis)
BuildRequires: pkgconfig(python)
BuildRequires: pyogg >= %pyoggversion
Requires: pyogg >= %pyoggversion
Url: https://ekyo.nerim.net/software/pyogg/index.html

%description
pyvorbis - a Python wrapper for the Ogg/Vorbis library

Ogg/Vorbis is available at http://www.xiph.org

This is the Vorbis module. You will need to download and install the
Python ogg module (available wherever you got this) before you can
build the vorbis module.


%prep
%setup -q -n %name-%version%prerel
%patch0 -p1 -b .unicode
%patch1 -p1 -b .python2.5
%patch2 -p0

%build
python config_unix.py
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT

%files
%doc README AUTHORS ChangeLog NEWS
%py_platsitedir/*




%changelog
* Thu Sep 15 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.5-0.a.5mdv2012.0
+ Revision: 699903
- fix build and underlinking issue, patch 2 (ty misc)

* Mon Nov 01 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.5-0.a.4mdv2011.0
+ Revision: 591601
- rebuild for python 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.5-0.a.3mdv2011.0
+ Revision: 442552
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.5-0.a.2mdv2009.1
+ Revision: 319586
- rebuild with python 2.6

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.5-0.a.1mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 30 2007 Götz Waschk <waschk@mandriva.org> 1.5-0.a.1mdv2008.0
+ Revision: 93999
- new version (fixes bug #28202 again)
- update patch 1

* Thu Sep 06 2007 Götz Waschk <waschk@mandriva.org> 1.4-2mdv2008.0
+ Revision: 80604
- bump release for bug #27632
- new version

* Wed Apr 25 2007 Götz Waschk <waschk@mandriva.org> 1.3-8mdv2008.0
+ Revision: 18131
- update patch 1


* Fri Feb 23 2007 Götz Waschk <waschk@mandriva.org> 1.3-7mdv2007.0
+ Revision: 124857
- fix bug #28202 (crash with python 2.5) with a patch from Ubuntu
- rediff patch 0

* Tue Nov 28 2006 Götz Waschk <waschk@mandriva.org> 1.3-6mdv2007.1
+ Revision: 88143
- Import pyvorbis

* Tue Nov 28 2006 G�tz Waschk <waschk@mandriva.org> 1.3-6mdv2007.1
- update file list

* Mon Dec 05 2005 Götz Waschk <waschk@mandriva.org> 1.3-5mdk
- Rebuild

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.3-4mdk
- Rebuild for new python

* Sat Sep 04 2004 G�tz Waschk <waschk@linux-mandrake.com> 1.3-3mdk
- fix URL

