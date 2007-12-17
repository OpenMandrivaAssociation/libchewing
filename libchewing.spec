%define version 0.3.091
%define release %mkrel 1

%define libname %mklibname chewing 3

%if %mdkversion < 1010
%define __libtoolize /bin/true
%endif

Name:		libchewing
Summary:	The intelligent phonetic input method library
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPL
Source0:	http://chewing.csie.net/download/libchewing/%{name}-%{version}.tar.bz2
URL:		http://chewing.csie.net/

%description
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.


%package data
Summary:	Data for Libchewing
Group:		System/Internationalization
#Requires:	%{libname} = %{version}-%{release}

%description data
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains data files from libchewing.

%package -n	%{libname}
Summary:	The intelligent phonetic input method library
Group:		System/Internationalization
Requires:       %{name}-data = %{version}
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains the basic libchewing library.

%package -n	%{libname}-devel
Summary:	Headers of libchewing for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains library and headers necessary for development
related to Chewing input method. You also need it if you want to
compile any input server that supports Chewing input method.


%prep
%setup -q

%build
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig


%files data
%defattr(-,root,root)
%doc COPYING
%{_datadir}/chewing

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*


