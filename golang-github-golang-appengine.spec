# https://github.com/golang/appengine
%global forgeurl        https://github.com/golang/appengine
%global goipath         google.golang.org/appengine
Version:                1.2.0

%gometa

Name:           golang-github-golang-appengine
Release:        1%{?dist}
Summary:        Go App Engine for Managed VMs
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock



%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(golang.org/x/text/encoding/htmlindex)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup

%build
%gobuildroot

%gobuild -o _bin/aebundler %{goipath}/cmd/aebundler
%gobuild -o _bin/aedeploy %{goipath}/cmd/aedeploy
%gobuild -o _bin/aefix %{goipath}/cmd/aefix

%install
%goinstall glide.lock glide.yaml

install -d -p %{buildroot}%{_bindir}
install -p -m 0755 _bin/aebundler %{buildroot}%{_bindir}
install -p -m 0755 _bin/aedeploy %{buildroot}%{_bindir}
install -p -m 0755 _bin/aefix %{buildroot}%{_bindir}

%check
%gochecks

%files
%license LICENSE
%doc README.md
%{_bindir}/aebundler
%{_bindir}/aedeploy
%{_bindir}/aefix

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Sat Oct 27 2018 Robert-André Mauchin <zebob.m@gmail.com> - 1.2.0-1
- Update to release 1.2.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 1.0.0-4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jun 10 2018 Jan Chaloupka <jchaloup@redhat.com> - 1.0.0-2
- Upload glide files

* Thu May 03 2018 Ed Marshall <esm@logic.net> - 1.0.0-1
- Bump to upstream 1.0.0 release
- Add golang-github-golang-appengine package with build/deploy tools

* Wed Mar 07 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.16.git4f7eeb5
- Update to spec 3.0

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.20160820git4f7eeb5
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.git4f7eeb5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.git4f7eeb5
- Bump to upstream 4f7eeb5305a4ba1966344836ba4af9996b7b4e05
  related: #1249049

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git6a43653
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git6a43653
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git6a43653
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git6a43653
- Bump to upstream 6a436539be38c296a8075a871cc536686b458371
  related: #1249049

* Thu Dec 15 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.git1c3fdc5
- Polish the spec file
  related: #1249049

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.git1c3fdc5
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git1c3fdc5
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.git1c3fdc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.git1c3fdc5
- Update to spec-2.1
  related: #1249049

* Fri Jul 31 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git1c3fdc5
- Update spec file to spec-2.0
  resolves: #1249049

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git1c3fdc5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 22 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git1c3fdc5
- First package for Fedora
  resolves: #1185082

