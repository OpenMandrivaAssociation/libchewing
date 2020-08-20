%define major	3
%define libname %mklibname chewing %{major}
%define devname %mklibname chewing -d

Summary:	Intelligent phonetic input method library
Name:		libchewing
Version:	0.5.1
Release:	1
License:	GPLv2
Group:		System/Libraries
Url:		http://chewing.im/
Source0:	https://github.com/chewing/libchewing/archive/v%{version}.tar.gz
Requires:	%{libname} = %{EVRD}
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	texinfo

%description
Phonetic input method library for Chinese

%package -n %{libname}
Summary:	Phonetic input method library for Chinese
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Phonetic input method library for Chinese

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# No need to package static libs
rm -f %{buildroot}%{_libdir}/*.a

%files
%{_datadir}/libchewing

%files -n %{libname}
%{_libdir}/libchewing.so.%{major}*

%files -n %{devname}
%{_libdir}/libchewing.so
%{_libdir}/pkgconfig/chewing.pc
%{_infodir}/libchewing.info*
%{_includedir}/chewing
