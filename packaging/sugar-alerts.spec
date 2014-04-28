name:           sugar-alerts
Version:        0.1.0
Release:        1
Summary:        Set of default message notifications for Sugar

License:        GPLv2+
URL:            https://github.com/tchx84/sugar-alerts
Source0:        %{name}-%{version}.tar.gz

Requires:       python >= 2.7, sugar >= 0.101

BuildArch:      noarch

%description
This package allows  Sugar to display default message notifications for system-wide events.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/sugar/extensions/webservice/
cp -r extensions/webservice/alerts $RPM_BUILD_ROOT/%{_datadir}/sugar/extensions/webservice/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/sugar/extensions/webservice/alerts

%changelog
* Mon Apr 28 2014 Martin Abente Lahaye <tch@sugarlabs.org>
- initial release
