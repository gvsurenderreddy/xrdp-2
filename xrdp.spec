Summary:	Open source remote desktop protocol (RDP) server
Name:		xrdp
Version:	0.4.0
Release:	%mkrel 0.1
License:	GPL
Group:		System/Servers
URL:		http://xrdp.sourceforge.net/
Source0:	http://dl.sf.net/xrdp/xrdp-%{version}.tar.gz
Patch0:		xrdp-0.4.0-sesman.patch
Patch1:		xrdp-0.4.0-sesmantools.patch
Patch2:		xrdp-0.4.0-docs.patch
Patch3:		xrdp-optflags.diff
Patch4:		xrdp-no_rpath.diff
BuildRequires:	pam-devel
BuildRequires:	openssl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The goal of this project is to provide a fully functional Linux terminal
server, capable of accepting connections from rdesktop and Microsoft's own
terminal server / remote desktop clients.

%prep

%setup -q

%patch0
%patch1
%patch2
%patch3 -p1
%patch4 -p1

%{__perl} -pi.orig -e 's|/lib\b|/%{_lib}|g' Makefile */Makefile

%build
%serverbuild
make

%install
rm -rf %{buildroot}

make installdeb DESTDIRDEB="%{buildroot}"

install -Dp -m0755 sesman/libscp/libscp.so %{buildroot}%{_libdir}/xrdp/libscp.so

### Clean up buildroot
rm -rf %{buildroot}%{_sysconfdir}/init.d/xrdp_control.sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING *.txt instfiles/*.sh
%dir %{_sysconfdir}/xrdp
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/xrdp/*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pam.d/sesman
%dir %{_libdir}/xrdp
%attr(0755,root,root) %{_libdir}/xrdp/*.so
%attr(0644,root,root) %{_libdir}/xrdp/ad256.bmp
%attr(0644,root,root) %{_libdir}/xrdp/cursor0.cur
%attr(0644,root,root) %{_libdir}/xrdp/cursor1.cur
%attr(0755,root,root) %{_libdir}/xrdp/sesman
%attr(0755,root,root) %{_libdir}/xrdp/startwm.sh
%attr(0644,root,root) %{_libdir}/xrdp/Tahoma-10.fv1
%attr(0755,root,root) %{_libdir}/xrdp/xrdp
%attr(0644,root,root) %{_libdir}/xrdp/xrdp256.bmp
%attr(0644,root,root) %{_mandir}/man5/*.5*
%attr(0644,root,root) %{_mandir}/man8/*.8*
