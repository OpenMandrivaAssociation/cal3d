%define major 12
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	A skeletal based character animation library
Name:		cal3d
Version:	0.11.0
Release:	%mkrel 7
Group:		System/Libraries
License:	LGPLv2+
URL:		http://gna.org/projects/cal3d/
Source0:	http://download.gna.org/cal3d/sources/%{name}-%{version}.tar.bz2
BuildRequires:  valgrind
BuildRequires:	doxygen
BuildRequires:	docbook-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Obsoletes:	%mklibname %{name} -d 12

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use Cal3D.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}_converter
%{_mandir}/man1/%{name}_converter.1*
