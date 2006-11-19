%define 	module	        pylons
%define     fname           Pylons
%define     python_version  2.4
Summary:	Pylons Web Framework
Summary(pl):	Środowisko Pylons
Name:		python-%{fname}
Version:	0.9.3
Release:	0.1
License:	BSD
Group:		Libraries/Python
Source0:    http://cheeseshop.python.org/packages/source/P/%{fname}/%{fname}-%{version}.tar.gz
# Source0-md5:   1c36a3d58d81281a0f252a747ad38a00
URL:		http://pylonshq.com/
BuildRequires:  python-setuptools
Requires:	python >= %{python_version}
Requires:   python-Paste
Requires:   python-PasteDeploy
Requires:   python-simplejson
Requires:   python-FormEncode
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pylons is a lightweight web framework emphasizing
flexibility and rapid development.

%description -l pl
Pylons to nieduże środowisko do szybkiego i elastycznego
tworzenia interaktywnych stron WWW.

%prep
%setup -qn %{fname}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/%{module}/decorators/*.py[co]
%{py_sitescriptdir}/%{module}/i18n/*.py[co]
