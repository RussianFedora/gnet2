Name:           gnet2
Version:        2.0.8
Release:        6%{?dist}
Summary:        A simple network library built upon glib

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gnetlibrary.org/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/gnet/2.0/gnet-%{version}.tar.bz2
Patch1:         gnet2-2.0.8-build.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  glib2-devel

%description
GNet is a simple network library. It is written in C, object-oriented, and
built upon GLib. It is intended to be easy to use and port.

%package        devel
Summary:        Headers and libraries for building apps that use gnet2
Group:          Development/Libraries
Requires:       %{name} = %{version} glib2-devel

%description    devel
This package contains headers and libraries required to build applications that
use GNet 2.

%prep
%setup -q -n gnet-%{version}
%patch1 -p1 -b .build

%build
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS BUGS COPYING NEWS README TODO
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc HACKING
%{_datadir}/aclocal/*
%{_datadir}/gtk-doc/html/gnet
%{_includedir}/*
%{_libdir}/gnet-*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Feb 16 2010 Tomas Mraz <tmraz@redhat.com> 2.0.8-4
- Fix FTBFS due to linker and gcc changes (#564691)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jun  5 2008 Tomas Mraz <tmraz@redhat.com> 2.0.8-1
- upgrade to new upstream release

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.7-11
- Autorebuild for GCC 4.3

* Tue Aug 21 2007 Tomas Mraz <tmraz@redhat.com> 2.0.7-10
- license tag fix

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2.0.7-9
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Wed Sep 20 2006 Tomas Mraz <tmraz@redhat.com> 2.0.7-8
- Rebuild for Fedora Extras 6

* Mon Feb 13 2006 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-6
- Rebuild for Fedora Extras 5

* Wed Nov  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-5
- Removed static libs
- Removed .la

* Tue Jun 21 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-4
- Added .so to -devel (#161283)
- Cleaned up %%changelog

* Mon May  9 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-3
- Added disttag

* Mon Apr 11 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-3
- Added glib2-devel to Requires of -devel

* Mon Apr 11 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-2
- Minor specfile cleanups

* Wed Mar 30 2005 Ignacio Vazquez-Abrams <ivazquez@ivazquez.net> 2.0.7-1
- Initial RPM release
