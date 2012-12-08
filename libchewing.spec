%define major 3
%define libname %mklibname chewing %{major}
%define develname %mklibname chewing -d

Name:		libchewing
Summary:	The intelligent phonetic input method library
Epoch:		1
Version:	0.3.3
Release:	3
Group:		System/Internationalization
License:	LGPLv2+
Source0:	http://chewing.csie.net/download/libchewing/%{name}-%{version}.tar.bz2
URL:		http://chewing.csie.net/

%description
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

%package data
Summary:	Data for Libchewing
Group:		System/Internationalization

%description data
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains data files from libchewing.

%package -n	%{libname}
Summary:	The intelligent phonetic input method library
Group:		System/Internationalization
Requires:	%{name}-data = %{EVRD}
Provides:	%{name} = %{EVRD}

%description -n %{libname}
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains the basic libchewing library.

%package -n	%{develname}
Summary:	Headers of libchewing for development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel= %{EVRD}

%description -n %{develname}
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains library and headers necessary for development
related to Chewing input method. You also need it if you want to
compile any input server that supports Chewing input method.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files data
%doc COPYING
%{_datadir}/chewing

%files -n %{libname}
%doc COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*


%changelog
* Wed Apr 13 2011 Funda Wang <fwang@mandriva.org> 1:0.3.3-1mdv2011.0
+ Revision: 652852
- new version 3.3.

* Sat Jul 24 2010 Funda Wang <fwang@mandriva.org> 1:0.3.2-4.svn1051.1mdv2011.0
+ Revision: 558206
- New snapshot to fix mdv#60301

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.3.2-3mdv2010.1
+ Revision: 520760
- rebuilt for 2010.1

* Sun Jan 04 2009 Emmanuel Andry <eandry@mandriva.org> 1:0.3.2-2mdv2009.1
+ Revision: 324484
- New version 0.3.2
- define major as a var

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 1:0.3.1-2mdv2009.1
+ Revision: 292355
- fix requires on libname

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 1:0.3.1-1mdv2009.1
+ Revision: 292073
- add epoch to ease upgrade
- New version 0.3.1

* Mon Aug 25 2008 Funda Wang <fwang@mandriva.org> 0.3.091-3.836.2mdv2009.0
+ Revision: 275853
- New svn snapshot

* Wed Jun 18 2008 Funda Wang <fwang@mandriva.org> 0.3.091-3.830.1mdv2009.0
+ Revision: 224731
- BR check
- Update to latest svn source

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.3.091-2mdv2008.1
+ Revision: 150508
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Jan 09 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.3.091-1mdv2007.0
+ Revision: 106768
- Import libchewing

* Mon Dec 04 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.3.091-1mdv2007.1
- new release

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.3.0-1mdv2007.0
- new release (major was bumped)

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.2.7-2mdk
- Rebuild

* Tue Aug 16 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.2.7-1mdk
- new release from You-Cheng Hsieh <yochenhsieh@xuite.net>
- mkrel

* Tue Jun 21 2005 Abel Cheung <deaddog@mandriva.org> 0.2.6-2mdk
- Rebuild

* Fri Mar 04 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.2.6-1mdk
- new release

* Sat Jan 01 2005 Abel Cheung <deaddog@mandrakesoft.com> 0.2.5-1mdk
- New release 0.2.5
- rpmlint fixes

* Fri Dec 24 2004 Abel Cheung <deaddog@mandrake.org> 0.2.4-1mdk
- First Mandrakelinux package, thanks to the work done by
  Shiva Huang <blueshiva@giga.net.tw> and
  UTUMI Hirosi <utuhiro78@yahoo.co.jp>.

