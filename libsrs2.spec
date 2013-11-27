Name:		libsrs2
Summary:	Next generation SRS library
Version:	1.0.18
Release:	0%{?dist}
License:	SRS Library
Group:		System Environment/Libraries
URL:		http://www.libsrs2.org/
Source0:	http://www.libsrs2.org/srs/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
Obsoletes:	libsrs2-toaster
BuildRoot:      %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

%define debug_package %{nil}

#-------------------------------------------------------------------------------
%description
#-------------------------------------------------------------------------------
SRS implementation library.

%package -n %{name}-devel
Summary:	SRS library build/development
Group:		System Environment/Libraries
%description -n %{name}-devel
SRS build/development library, for building packages which use libsrs2.

#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -q

perl -pi -e's/CFLAGS=/CFLAGS=%{optflags} -fPIC /' Makefile

#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------
./configure --prefix=%{_prefix} --libdir=%{_libdir}

make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

#-------------------------------------------------------------------------------
%clean
#-------------------------------------------------------------------------------
rm -rf %{buildroot}

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------
%defattr(-,root,root,-)
%{_libdir}/libsrs2.so*

#-------------------------------------------------------------------------------
%files -n %{name}-devel
#-------------------------------------------------------------------------------
%defattr(-,root,root,-)
%doc ChangeLog INSTALL README NEWS AUTHORS COPYING
%{_bindir}/srs
%{_libdir}/libsrs2.a
%{_libdir}/libsrs2.la
%{_includedir}/srs2.h

#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Fri Nov 15 2013 Eric Shubert <eric@datamatters.us> 1.0.18-0.qt
- Migrated to github
- changed package to libsrs2, libsrs2-devel packages
- Added CentOS 6 support
- Removed unsupported cruft
* Fri Jun 12 2009 Jake Vickers <jake@qmailtoaster.com> 1.0.18-1.3.6
- Added Fedora 11 support
- Added Fedora 11 x86_64 support
* Tue Jun 02 2009 Jake Vickers <jake@qmailtoaster.com> 1.0.18-1.3.6
- Added Mandriva 2009 support
* Wed Apr 22 2009 Jake Vickers <jake@qmailtoaster.com> 1.0.18-1.3.5
- Added Fedora 9 x86_64 and Fedora 10 x86_64 support
* Fri Feb 13 2009 Jake Vickers <jake@qmailtoaster.com> 1.0.18-1.3.4
- Added Suse 11.1 support
* Sun Feb 08 2009 Jake Vickers <jake@qmailtoaster.com> 1.0.18-1.3.4
- Added Fedora 9 and 10 support
* Sat Apr 14 2007 Nick Hemmesch <nick@ndhsoft.com> 1.0.18-1.3.3
- Added CentOS 5 i386 support
- Added CentOS 5 x86_64 support
* Fri Jan 12 2007 Erik A. Espinoza <espinoza@kabewm.com> 1.0.18-1.3.2
- Minor corrections for 64-bit, Fedora
* Tue Jan 02 2007 Erik A. Espinoza <espinoza@kabewm.com> 1.0.18-1.3.1
- Initial Package
