%define version 0.3.091
%define svnrel 836
%define release %mkrel 3.%{svnrel}.1

%define libname %mklibname chewing 3
%define develname %mklibname chewing -d

Name:		libchewing
Summary:	The intelligent phonetic input method library
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	LGPLv2+
Source0:	http://chewing.csie.net/download/libchewing/%{name}-%{version}-r%{svnrel}.tar.bz2
URL:		http://chewing.csie.net/
BuildRequires:	check-devel
Buildroot:      %_tmppath/%{name}-%{version}-%{release}-root

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
Requires:       %{name}-data = %{version}
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains the basic libchewing library.

%package -n	%{develname}
Summary:	Headers of libchewing for development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d chewing 3

%description -n %{develname}
libchewing is an intelligent Chinese phonetic input method library
which is also know as Qooing. Based on Chewing input method.

This package contains library and headers necessary for development
related to Chewing input method. You also need it if you want to
compile any input server that supports Chewing input method.


%prep
%setup -q -n %name

%build
./autogen.sh
%configure2_5x 
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


%files data
%defattr(-,root,root)
%doc COPYING
%{_datadir}/chewing

%files -n %{libname}
%defattr(-,root,root)
%doc COPYING
%{_libdir}/lib*.so.3*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_libdir}/pkgconfig/*
%{_includedir}/*
