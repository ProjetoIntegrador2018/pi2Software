<p align="center"><a href="https://i.imgur.com/vh3ta7o.jpg" target="_blank"><img width="600"src="https://i.imgur.com/vh3ta7o.jpg"></a></p>

![build](https://api.travis-ci.org/ProjetoIntegrador2018/pi2Software.svg?branch=master)

### ℹ️ Sobre

<p justify="align">Repositório oficial do grupo responsável pelo desenvolvimento de um case afinador de violão automático da disciplina Projeto Integrador 2 da Universidade de Brasília, campus Gama.</p>

### ℹ️ Repositório com documentação e desenhos esquemáticos

Utilizando o comando em destaque é possível baixar todo o conteúdo de documentação do projeto. A documentação também pode ser acessada através da [Wiki](https://github.com/ProjetoIntegrador2018/pi2Software/wiki).

```Terminal
$ git clone https://github.com/ProjetoIntegrador2018/pi2Software.wiki.git
```

###  ℹ️️ Configuração de Ambiente

<p align="justify">Para iniciar a configuração do ambiente necessário para o desenvolvimento, siga os passos abaixo.</p>

- 1º Instale o [VirtualBox](https://www.virtualbox.org/);
- 2º Instale o [Vagrant](https://www.vagrantup.com/downloads.html);
- 3º No terminal da máquina hospedeira, digite:

```Terminal
$ sudo vagrant up
```
<p justify="align">Ao término da instalação, a máquina virtual abrirá automaticamente, siga os passos a seguir para continuar a configuração do ambiente.</p>

- <p justify="align">Como mostrado abaixo, abra o painel de configuração da raspberry.</p>

<p align="center"><a href="https://i.imgur.com/nV8yxoD.jpg" target="_blank"><img width="600"src="https://i.imgur.com/nV8yxoD.jpg"></a></p>

- Altere a senha para: 12345
<p align="center"><a href="https://i.imgur.com/axVrILs.jpg" target="_blank"><img width="600"src="https://i.imgur.com/axVrILs.jpg"></a></p>

- Habilite a opção SSH
<p align="center"><a href="https://i.imgur.com/TzwfhT0.jpg" target="_blank"><img width="600"src="https://i.imgur.com/TzwfhT0.jpg"></a></p>


- <p justify="align">Ajuste a resolução da máquina virtual de acordo com as configurações de resolução da máquina hospedeira.</p>
- <p justify="align">Obs: Caso não seja apresentado opções de resolução, siga para o próximo passo e após o seu término tente alterar novamente a resolução e reinicie novamente.</p>
<p align="center"><a href="https://i.imgur.com/r2V1bEo.png" target="_blank"><img width="600"src="https://i.imgur.com/r2V1bEo.png"></a></p>

- <p justify="align">Desligue o sistema hospedado e logo em seguida, no terminal da máquina hospedeira, digite:</p>

```Terminal
$ sudo vagrant up
```
