# count_files.spec

Name:           count_files
Version:        1.0
Release:        1%{?dist}
Summary:        Count files /etc
Group:          Applications/System
License:        GPL
URL:            https://github.com/Tarasdd/labs_os
BuildArch:      noarch

%description
This package counts the number of files in the /etc directory.

%prep
if [ ! -d labsOC ]; then
  git clone https://github.com/Tarasdd/labs_os.git labs_os
fi
cd labs_os/

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 0755 count_files.sh $RPM_BUILD_ROOT%{_bindir}/%{name}.sh

%files
%{_bindir}/%{name}.sh
