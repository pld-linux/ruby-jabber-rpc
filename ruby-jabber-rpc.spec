%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
Summary:	Jabber-RPC library for Ruby
Summary(pl):	Biblioteka Jabber-RPC dla jêzyka Ruby
Name:		ruby-jabber-rpc
Version:	0.0.20041208
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://jabber-rpc.rubyforge.org/jabber-rpc.tar.gz
# Source0-md5:	340021bcf4b1dabbfc7f1153e7e5cc73
Source1:	setup.rb
URL:		http://jabber-rpc.rubyforge.org/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
Requires:	ruby-jabber4r
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jabber-RPC library for Ruby.

%description -l pl
Biblioteka Jabber-RPC dla jêzyka Ruby.

%prep
%setup -q -n jabber-rpc

%build
mkdir lib/jabber -p
mv rpc.rb lib/jabber/rpc.rb
install %{SOURCE1} setup.rb
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

ruby setup.rb setup

rdoc -o rdoc/ --main README README lib/* --title "%{name} %{version}" --inline-source
rdoc --ri -o ri lib/*

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/jabber/rpc.rb
# Does not merge well with others.
%{ruby_ridir}/Jabber/RPC
