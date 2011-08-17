Name:           unique
Version:        1.1.4
Release:        2%{?dist}
Summary:        Single instance support for applications

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.gnome.org/~ebassi/source/
Source0:        http://download.gnome.org/sources/libunique/1.1/libunique-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  dbus-glib-devel
BuildRequires:  gnome-doc-utils >= 0.3.2
BuildRequires:  libtool
BuildRequires:  glib2-devel >= 2.12.0
BuildRequires:  gtk2-devel >= 2.11.0
BuildRequires:  gtk-doc

%description
Unique is a library for writing single instance applications, that is
applications that are run once and every further call to the same binary
either exits immediately or sends a command to the running instance.

%package devel
Summary: Libraries and headers for Unique
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: gtk-doc
Requires: dbus-glib-devel
Requires: gtk2-devel

%description devel
Headers and libraries for Unique.

%prep
%setup -q -n libunique-%{?version}

%build
%configure --disable-gtk-doc --disable-static --enable-introspection=no
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/gtk-doc/html/unique/
%{_includedir}/unique-1.0/
%{_libdir}/pkgconfig/*
%{_libdir}/lib*.so

%changelog
* Mon May  3 2010 Matthias Clasen <mclasen@redhatcom> - 1.1.4-2
- Don't rebuild docs to avoid multilib conflicts
Resolves: #587221

* Thu Nov 12 2009 Richard Hughes  <rhughes@redhat.com> - 1.1.4-1
- Update to 1.1.4
- Fixes nautilus segfaulting when launched from Places or the trash applet.

* Tue Aug 25 2009 Matthias Clasen <mclasen@redhatcom> - 1.1.2-1
- Update to 1.1.2

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Richard Hughes  <rhughes@redhat.com> - 1.0.8-1
- Update to latest upstream version
 * Unbreak subclassing of UniqueApp
 * Remove upstreamed patches

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 20 2008 Matthias Clasen  <mclasen@redhat.com> - 1.0.4-3
- Actually apply the patch

* Sat Dec 20 2008 Matthias Clasen  <mclasen@redhat.com> - 1.0.4-2
- Fix a nautilus segfault

* Mon Nov 24 2008 Richard Hughes  <rhughes@redhat.com> - 1.0.4-1
- Update to latest upstream version
 * Plug a leak in UniqueMessageData
 * Fix linking with --as-needed
 * Do not export private functions symbols

* Sat Nov 22 2008 Richard Hughes  <rhughes@redhat.com> - 1.0.0-2
- Fix up summary text

* Thu Jul 31 2008 Richard Hughes  <rhughes@redhat.com> - 1.0.0-1
- Update to latest upstream version
 * First stable release
 * API is frozen
 * D-Bus and socket backends supported

* Fri May 16 2008 Richard Hughes  <rhughes@redhat.com> - 0.9.4-5
- More updates to the spec file from Dan Horak, rh#446407

* Thu May 15 2008 Richard Hughes  <rhughes@redhat.com> - 0.9.4-4
- Updates to the spec file from Dan Horak, rh#446407

* Thu May 08 2008 Richard Hughes  <rhughes@redhat.com> - 0.9.4-3
- Initial version

