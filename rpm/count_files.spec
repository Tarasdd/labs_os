Name:           count_files
Version:        1.0
Release:        1%{?dist}
Summary:        Count files in /etc directory
Group:          Applications/System
License:        GPL
URL:            https://github.com/Tarasdd/labs_os
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package counts the number of files in the /etc directory.

%prep
%setup -q -n labs_os

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 $RPM_BUILD_DIR/labs_os/count_files.sh $RPM_BUILD_ROOT/%{_bindir}/%{name}.sh

%files
/usr/bin/count_files.sh


