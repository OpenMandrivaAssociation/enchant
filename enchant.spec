%define major 1
%define libname %mklibname enchant %{major}
%define develname %mklibname enchant -d

Summary:	An enchanting spell checking library
Name:		enchant
Version:	1.5.0
Release:	%mkrel 1
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.abisource.com/enchant/
Source0:	http://www.abisource.com/downloads/enchant/%{version}/%{name}-%{version}.tar.gz
# mpol: change default ordering for nl; first myspell
Patch0:		enchant-1.2.0-ordering-nl.patch
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	aspell-devel
BuildRequires:	pkgconfig
%if %mdkversion >= 200700
# hspell check uses -lz:
BuildRequires:	zlib-devel
BuildRequires:	hspell-devel
BuildRequires:	voikko-devel
BuildRequires:	dbus-glib-devel
%endif
%if %mdkversion > 200800
BuildRequires:	hunspell-devel
%endif
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
A library that wraps other spell checking backends.

%package -n %{libname}
Summary:	Libraries for enchant
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package provides the libraries for using enchant.

%package -n %{develname}
Summary:	Libraries and include files for developing with enchant
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{mklibname enchant 1}-devel = %{version}-%{release}
Obsoletes:	%{mklibname enchant 1}-devel

%description -n	%{develname}
This package provides the necessary development libraries and include
files to allow you to develop with enchant.

%prep

%setup -q
%patch0 -p0 -b .ordering-nl

# lib64 fix
perl -pi -e "s|/lib\b|/%{_lib}|g" configure*

# antibork
perl -pi -e "s|^automake --version|#automake --version|g" ./autogen.sh

%build
# this fixes bad relinking (rpath)
rm -f configure
autoreconf --force --install

%configure2_5x \
     --with-myspell-dir=%{_datadir}/dict/ooo

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS HACKING README TODO
%{_bindir}/*
%{_datadir}/enchant
%{_mandir}/man1/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/lib*.so.%{major}*
%dir %{_libdir}/enchant
# todo: split backends in seperate packages?
# (anssi) Nope. Nothing would pull them, then.
# But we could move them to /usr/lib/enchant-%major/
# to allow simultaneous installation with future
# libenchant2.
# (anssi) or move them to lib(64)enchant-modules,
# required by lib(64)enchantN
%{_libdir}/enchant/lib*.so*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/lib*.so
%attr(644,root,root) %{_libdir}/*.la
%{_libdir}/*.a
#%{_libdir}/enchant/*.so
%{_libdir}/enchant/*.a
%attr(644,root,root) %{_libdir}/enchant/*.la
%{_libdir}/pkgconfig/enchant.pc
%dir %{_includedir}/enchant
%{_includedir}/enchant/*
