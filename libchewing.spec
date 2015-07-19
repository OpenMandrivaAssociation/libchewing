%define major 3
%define libname %mklibname chewing %{major}
%define develname %mklibname chewing -d

Name:		libchewing
Summary:	The intelligent phonetic input method library
Epoch:		1
Version:	0.4.0
Release:	3
Group:		System/Internationalization
License:	LGPLv2+
Source0:	https://github.com/chewing/libchewing/releases/download/v0.4.0/%{name}-%{version}.tar.bz2
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
# %{_libdir}/libchewing
%{_infodir}/*
%{_datadir}/libchewing/dictionary.dat
%{_datadir}/libchewing/index_tree.dat
%{_datadir}/libchewing/pinyin.tab
%{_datadir}/libchewing/swkb.dat
%{_datadir}/libchewing/symbols.dat

%files -n %{libname}
%doc COPYING
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog NEWS 
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
