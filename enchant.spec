%define major 1
%define libname %mklibname enchant %{major}
%define devname %mklibname enchant -d
%define _disable_rebuild_configure 1

%define url_ver %(echo %{version} |sed -e 's,\\.,-,g')

Summary:	An enchanting spell checking library
Name:		enchant
Version:	1.6.1
Release:	6
License:	LGPLv2+
Group:		System/Libraries
Url:		https://abiword.github.io/enchant/
Source0:	https://github.com/AbiWord/enchant/archive/enchant-%{url_ver}/%{name}-%{version}.tar.gz
Patch0:		hunspell-1.4.0-has-no-limit.patch
BuildRequires:	aspell-devel
BuildRequires:	hspell-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(hunspell) >= 1.6.0
BuildRequires:	pkgconfig(libvoikko)
Conflicts:	%{libname} < 1.6.0-3

%description
A library that wraps other spell checking backends.

%package -n %{libname}
Summary:	Libraries for enchant
Group:		System/Libraries

%description -n %{libname}
This package provides the libraries for using enchant.

%package -n %{devname}
Summary:	Libraries and include files for developing with enchant
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package provides the necessary development libraries and include
files to allow you to develop with enchant.

%prep
%autosetup -n %{name}-%{name}-%{url_ver} -p1
./autogen.sh

%build
%configure \
	--enable-myspell \
	--with-myspell-dir=%{_datadir}/dict/ooo

%make_build LIBTOOLFLAGS="--tag=CC"

%install
%make_install

%files
%doc AUTHORS HACKING README TODO
%{_bindir}/*
%{_datadir}/enchant
%dir %{_mandir}/man1/*
%dir %{_libdir}/enchant
%{_libdir}/enchant/lib*.so*

%files -n %{libname}
%{_libdir}/libenchant.so.%{major}*

%files -n %{devname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/enchant.pc
%dir %{_includedir}/enchant
%{_includedir}/enchant/*
