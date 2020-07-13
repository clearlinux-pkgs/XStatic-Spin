#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Spin
Version  : 1.2.5.3
Release  : 26
URL      : https://files.pythonhosted.org/packages/a0/7a/598e72d65c1fca68aa1a47f62d6dd72ad8aa67ceaaa5a5193afc8ae9ada1/XStatic-Spin-1.2.5.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/a0/7a/598e72d65c1fca68aa1a47f62d6dd72ad8aa67ceaaa5a5193afc8ae9ada1/XStatic-Spin-1.2.5.3.tar.gz
Summary  : Spin 1.2.5 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Spin-python = %{version}-%{release}
Requires: XStatic-Spin-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
------------
        
        Spin JavaScript library packaged for setuptools (easy_install) / pip.
        
        This package is intended to be used by **any** project that needs these files.
        
        It intentionally does **not** provide any extra code except some metadata
        **nor** has any extra requirements. You MAY use some minimal support code from
        the XStatic base package, if you like.
        
        You can find more info about the xstatic packaging way in the package `XStatic`.

%package python
Summary: python components for the XStatic-Spin package.
Group: Default
Requires: XStatic-Spin-python3 = %{version}-%{release}
Provides: xstatic-spin-python

%description python
python components for the XStatic-Spin package.


%package python3
Summary: python3 components for the XStatic-Spin package.
Group: Default
Requires: python3-core
Provides: pypi(xstatic_spin)

%description python3
python3 components for the XStatic-Spin package.


%prep
%setup -q -n XStatic-Spin-1.2.5.3
cd %{_builddir}/XStatic-Spin-1.2.5.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1587077612
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
