%define	name		cal3d
%define	version		0.11.0
#%define	cvs		cvs20050309
%define rel		%mkrel 5
%define	release		%rel
%define	lib_name_orig	lib%{name}
%define lib_major	12
%define lib_name	%mklibname %{name} %{lib_major}
%define	lib_name_devel	%mklibname %{name} %{lib_major} -d

Name:		%{name}
Summary:	A skeletal based character animation library
Version:	%{version}
Release:	%{release}
Group:		System/Libraries
License:	LGPL
URL:		http://cal3d.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:  libtool

%description
Cal3D is a skeletal based character animation library. It is platform-
independent and not bound to a specific graphic API. Originally designed to
be used in a 3d client for the Worldforge project (www.worldforge.org)
it evolved into a stand-alone product that can be used in many different
projects.

%package -n	%{lib_name}
Summary:	A skeletal based character animation library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with Cal3D.

%package -n	%{lib_name_devel}
Summary:	Headers for developing programs that will use Cal3D
Group:		Development/C++
Requires:	%{lib_name} = %{version}
Provides:	%{lib_name_orig}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{lib_name_devel}
This package contains the headers that programmers will need to develop
applications which will use Cal3D.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig
%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,0755)
%{_libdir}/%{lib_name_orig}.so.%{lib_major}*

%files -n %{lib_name_devel}
%defattr(-,root,root,0755)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.la
%{_libdir}/%{lib_name_orig}.so
#%{_libdir}/%{lib_name_orig}.la
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}_converter
%{_mandir}/man1/%{name}_converter.1*

