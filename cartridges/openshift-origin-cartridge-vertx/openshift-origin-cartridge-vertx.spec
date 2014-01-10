%global cartridgedir %{_libexecdir}/openshift/cartridges/vertx
%define vertx_name vert.x
%define vertx_version 2.1M3

Summary:       Provides Vertx.x support
Name:          openshift-origin-cartridge-vertx
Version: 1.0.0
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Source1:       http://dl.bintray.com/nscavell/vertx/%{vertx_name}-%{vertx_version}.tar.gz

Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel

BuildArch:     noarch

%description
Provides Vertx.x support to OpenShift. (Cartridge Format V2)

%prep
%setup -q
%setup -a 1

%build
%__rm %{name}.spec
%__rm -rf %{vertx_name}-%{vertx_version}/api-docs

# TODO: Change this to use vertx_version when 2.1 is out, as you can't have 2.1M3 as a version number in OpenShift
%__mkdir -p versions/2.1
%__mv %{vertx_name}-%{vertx_version} versions/2.1/dist

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Mon Jan 6 2014 Nick Scavelli <nscavell@redhat.com> 1.0.0-1
- Initial RPM spec
