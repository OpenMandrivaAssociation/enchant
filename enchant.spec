%define major 1
%define libname %mklibname enchant %{major}
%define develname %mklibname enchant -d

Summary:	An enchanting spell checking library
Name:		enchant
Version:	1.6.0
Release:	5
License:	LGPLv2+
Group:		System/Libraries
URL:		http://www.abisource.com/projects/enchant/
Source0:	http://www.abisource.com/downloads/enchant/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(glib-2.0)
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



%changelog
* Thu Dec 08 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.6.0-3
+ Revision: 738843
- removed find_lang
- rebuild
- removed .la files
- disabled static build
- removed defattr, mkrel, BuildRoot, clean section
- removed pre 200900 scriptlets
- moved backends to main pkg (not libs)

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.6.0-2
+ Revision: 655720
- clean up spec file

  + Ahmad Samir <ahmadsamir@mandriva.org>
    - rebuild

* Sat Jul 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6.0-1mdv2011.0
+ Revision: 554546
- update to new version 1.6.0
- drop patch 1, fixed by upstream

* Fri Feb 26 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.5.0-3mdv2010.1
+ Revision: 511545
- drop patch0, enchant defaults to using myspell, aspell, ispell, so no need to
  explicitly use that order for nl locale
- remove obsolete commands from .spec

* Tue Oct 27 2009 Frederic Crozat <fcrozat@mandriva.com> 1.5.0-2mdv2010.0
+ Revision: 459579
- Patch1 (SVN): fix incorrect dictonnary list in empathy (Abi bug #12305)

* Sun Jul 12 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.0-1mdv2010.0
+ Revision: 395054
- update to new version 1.5.0
- drop patch 1, fixed upstream

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.4.2-5mdv2009.1
+ Revision: 321097
- rediffed one fuzzy patch

* Fri Nov 28 2008 Götz Waschk <waschk@mandriva.org> 1.4.2-4mdv2009.1
+ Revision: 307452
- fix crash loading dictionaries (bug #45166)

* Mon Sep 22 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.2-3mdv2009.0
+ Revision: 286419
- build with support for hunspell

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.4.2-2mdv2009.0
+ Revision: 264458
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 06 2008 Anssi Hannula <anssi@mandriva.org> 1.4.2-1mdv2009.0
+ Revision: 202492
- run autoreconf --force --install instead of autogen.sh to fix build
- new version

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.4.1-1mdv2009.0
+ Revision: 195706
- new version
- drop patch 1, fixed upstream
- new license policy
- do not package COPYING.LIB file
- spec file clean

* Sat Jan 12 2008 Anssi Hannula <anssi@mandriva.org> 1.3.0-4mdv2008.1
+ Revision: 149641
- buildrequires zlib-devel for hspell engine

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3mdv2008.0
+ Revision: 74456
- fix build
- conform to the new devel naming


* Mon Feb 12 2007 Anssi Hannula <anssi@mandriva.org> 1.3.0-2mdv2007.0
+ Revision: 119044
- update patch1 with 1.3.0 compatible version from CVS

  + Laurent Montel <lmontel@mandriva.com>
    - Rebuild.........................
    - 1.3.0
    - Import enchant

* Wed Aug 23 2006 Anssi Hannula <anssi@mandriva.org> 1.2.6-2mdv2007.0
- add voikko provider plugin (patch1)
- fix buildrequires

* Tue Aug 01 2006 Jerome Soyer <saispo@mandriva.org> 1.2.6-1mdv2007.0
- New release 1.2.6

* Sat Mar 11 2006 Götz Waschk <waschk@mandriva.org> 1.2.3-1mdk
- New release 1.2.3

* Fri Nov 25 2005 Marcel Pol <mpol@mandriva.org> 1.2.0-2mdk
- P0: fix ordering for nl

* Thu Nov 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.0-1mdk
- 1.2.0
- added one lib64 fix
- don't nuke the *.la files

* Sun Jul 31 2005 Marcel Pol <mpol@mandriva.org> 1.1.5-3mdk
- define mysqldir at configure time
- %%mkrel

* Sat Jul 30 2005 Marcel Pol <mpol@mandriva.org> 1.1.5-2mdk
- add enchant.ordering
- for Dutch prefer myspell above aspell
- add symlink to myspell dictionaries

* Sat Dec 25 2004 Marcel Pol <mpol@mandrake.org> 1.1.5-1mdk
- 1.1.5

* Mon Sep 27 2004 Marcel Pol <mpol@mandrake.org> 1.1.2-3mdk
- move backend files from devel to library package

* Sat Jun 12 2004 Marcel Pol <mpol@mandrake.org> 1.1.2-2mdk
- rebuild

