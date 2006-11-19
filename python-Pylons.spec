%define 	module	        pylons
%define     fname           Pylons
%define     python_version  2.4
Summary:	Pylons Web Framework
Summary(pl):	Środowisko Pylons
Name:		python-%{fname}
Version:	0.9.3
Release:	0.2
License:	Pylons
Group:		Libraries/Python
Source0:    http://cheeseshop.python.org/packages/source/P/%{fname}/%{fname}-%{version}.tar.gz
# Source0-md5:   1c36a3d58d81281a0f252a747ad38a00
URL:		http://pylonshq.com/
BuildRequires:  python-setuptools
Requires:	python >= %{python_version}
Requires:   python-Paste
Requires:   python-PasteDeploy
Requires:   python-simplejson >= 1.4
Requires:   python-FormEncode >= 0.6
Requires:   python-Myghty >= 1.1
Requires:   python-MyghtyUtils >= 0.52
Requires:   python-Beaker >= 0.6.1
Requires:   python-WebHelpers >= 0.2.2
Requires:   python-Routes >= 1.5.2
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

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{fname}-%{version}-py%{python_version}.egg-info
