#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : XStatic-Spin
Version  : 1.2.5.2
Release  : 15
URL      : https://pypi.python.org/packages/source/X/XStatic-Spin/XStatic-Spin-1.2.5.2.tar.gz
Source0  : https://pypi.python.org/packages/source/X/XStatic-Spin/XStatic-Spin-1.2.5.2.tar.gz
Summary  : Spin 1.2.5 (XStatic packaging standard)
Group    : Development/Tools
License  : MIT
Requires: XStatic-Spin-python
BuildRequires : python-dev
BuildRequires : setuptools

%description
XStatic-Spin
--------------
Spin JavaScript library packaged for setuptools (easy_install) / pip.

%package python
Summary: python components for the XStatic-Spin package.
Group: Default

%description python
python components for the XStatic-Spin package.


%prep
%setup -q -n XStatic-Spin-1.2.5.2

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
