Name:           galileo-mura
Version:        0.0.git.1771.a1e55faa
Release:        1%{?dist}
Summary:        Utilities for setting and reading mura correction on Galileo
License:        MIT
URL:            https://github.com/ublue-os/bazzite

Source0:        %{name}-extractor-%{version}.tar.xz

BuildRequires:  systemd-rpm-macros
BuildRequires:  gcc
BuildRequires:  meson >= 0.54.0
BuildRequires:  ninja-build

%description
Utilities for setting and reading mura correction on Galileo

# Disable debug packages
%define debug_package %{nil}

%prep
%autosetup -n %{name}-extractor-%{version}

%build
%meson
%meson_build

%install
%meson_install

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE
%attr(4755, root, root) %{_bindir}/galileo-mura-extractor
%{_bindir}/galileo-mura-setup
%{_bindir}/galileo-mura-download

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
