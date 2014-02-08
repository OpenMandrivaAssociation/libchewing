%define major	3
%define libname	%mklibname chewing %{major}
%define devname	%mklibname chewing -d

Summary:	The intelligent phonetic input method library
Name:		libchewing
Epoch:		1
Version:	0.3.3
Release:	4
Group:		System/Internationalization
License:	LGPLv2+
Url:		http://chewing.csie.net/
Source0:	http://chewing.csie.net/download/libchewing/%{name}-%{version}.tar.bz2

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

%package -n	%{devname}
Summary:	Headers of libchewing for development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel= %{EVRD}

%description -n %{devname}
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
%{_libdir}/libchewing.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

