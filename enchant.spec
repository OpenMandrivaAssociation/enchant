%define major 1
%define libname %mklibname enchant %{major}
%define develname %mklibname enchant -d

Summary:	An enchanting spell checking library
Name:		enchant
Version:	1.6.0
Release:	3
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.abisource.com/projects/enchant/
Source0:	http://www.abisource.com/downloads/enchant/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	aspell-devel
BuildRequires:	hspell-devel
BuildRequires:	voikko-devel
BuildRequires:	hunspell-devel
Conflicts:	%{libname} < 1.6.0-3

%description
A library that wraps other spell checking backends.

%package -n %{libname}
Summary:	Libraries for enchant
Group:		System/Libraries

%description -n	%{libname}
This package provides the libraries for using enchant.

%package -n %{develname}
Summary:	Libraries and include files for developing with enchant
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package provides the necessary development libraries and include
files to allow you to develop with enchant.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--with-myspell-dir=%{_datadir}/dict/ooo

%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name "*.la" -delete

%files
%doc AUTHORS HACKING README TODO
%{_bindir}/*
%{_datadir}/enchant
%{_mandir}/man1/*
%dir %{_libdir}/enchant
%{_libdir}/enchant/lib*.so*

%files -n %{libname}
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/enchant.pc
%dir %{_includedir}/enchant
%{_includedir}/enchant/*

