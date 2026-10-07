Name:           oowc
Version:        0.1.0
Release:        1%{?dist}
Summary:        SIMD-accelerated newline, word, UTF-8 rune, and byte counter for massive files.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oowc
Source0:        oowc-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oowc is a sovereign, capability-bounded METRIC COUNTER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oowc
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oowc-uninstall

%files
/usr/bin/oowc
/usr/bin/oowc-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
