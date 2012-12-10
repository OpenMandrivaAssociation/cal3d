%define major 12
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A skeletal based character animation library
Name:		cal3d
Version:	0.11.0
Release:	11
Group:		System/Libraries
License:	LGPLv2+
URL:		http://gna.org/projects/cal3d/
Source0:	http://download.gna.org/cal3d/sources/%{name}-%{version}.tar.bz2
Patch0:		cal3d-0.11.0-gcc43.patch
BuildRequires:	valgrind
BuildRequires:	doxygen
BuildRequires:	docbook-utils

%description
Cal3D is a skeletal based character animation library. It is platform-
independent and not bound to a specific graphic API. Originally designed to
be used in a 3d client for the Worldforge project (www.worldforge.org)
it evolved into a stand-alone product that can be used in many different
projects.

%package -n %{libname}
Summary:	A skeletal based character animation library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Cal3D is a skeletal based character animation library. It is platform-
independent and not bound to a specific graphic API. Originally designed to
be used in a 3d client for the Worldforge project (www.worldforge.org)
it evolved into a stand-alone product that can be used in many different
projects.

%package -n %{develname}
Summary:	Headers for developing programs that will use Cal3D
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use Cal3D.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}_converter
%{_mandir}/man1/%{name}_converter.1*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.11.0-10mdv2011.0
+ Revision: 616909
- the mass rebuild of 2010.0 packages

* Mon Oct 05 2009 Emmanuel Andry <eandry@mandriva.org> 0.11.0-9mdv2010.0
+ Revision: 453947
- fix build with p0 (gcc issue)

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Fri Apr 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.11.0-7mdv2009.0
+ Revision: 195681
- new license policy
- new development library policy
- fix descriptions
- spec file clean

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 25 2007 Emmanuel Andry <eandry@mandriva.org> 0.11.0-6mdv2008.1
+ Revision: 137808
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import cal3d


* Thu Sep 21 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.11.0-5mdv2007.0
- do not remove converter

* Fri Jul 07 2006 Emmanuel Andry <eandry@mandriva.org> 0.11.0-1mdv2007.0
- 0.11.0

* Wed Apr 26 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.10.1-0.cvs20050309.4mdk
- Add BuildRequires

* Fri Mar 11 2005 Olivier Thauvin <nanardon@mandrake.org> 0.10.1-0.cvs20050309.3mdk
- %%mkrel
- move .la from lib to devel

* Wed Mar 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.10.1-0.cvs20050309.2mdk
- gah, actually package the cvs release *mumble*

* Wed Mar 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.10.1-0.cvs20050309.1mdk
- update from cvs

* Wed Mar 09 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.10.0-1mdk
- 0.10.0

* Thu Dec 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.1-4mdk
- rebuild

* Tue Jun 15 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.1-3mdk
- rebuild

* Sun Dec 28 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.1-2mdk
- fix so name (from Luca Berra)

* Tue Dec 23 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.9.1-1mdk
- 0.9.1

* Tue Jul 08 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8-3mdk
- fix unowned dir reported by Oliviers distriblint bot

* Tue May 06 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8-2mdk
- rebuild for rpm-4.2
- use %%mklibname for devel package

* Sat Apr 26 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8-1mdk
- spec file fixes
- from Jean-Baptiste Lamy <jiba@tuxfamily.org> 0.8-1mdk
  - First RPM release
