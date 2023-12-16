Summary: A script to count files in /etc
Name: count_files
Version: 1.0
Release: 1%{?dist}
License: MIT

%description
This script counts files in the /etc directory.

%prep
# Нет необходимости в этом разделе для данного примера

%build
# Нет необходимости в этом разделе для данного примера

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 count_files.sh %{buildroot}/home/taras/labs/count_files.sh

%files
%defattr(-,root,root,-)
/home/taras/labs/count_files.sh
