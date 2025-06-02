# Project Management Tool

[English](#english) | [Português](#português)

## English

### Overview
Comprehensive project management tool built with Python and Flask. Features project creation, task management, team collaboration, progress tracking, and analytics dashboard. Designed for efficient project planning and execution with modern web interface.

### Features
- **Project Management**: Create and manage multiple projects
- **Task Tracking**: Comprehensive task creation and assignment
- **Team Collaboration**: User management and role-based access
- **Progress Monitoring**: Real-time project progress tracking
- **Analytics Dashboard**: Project insights and performance metrics
- **File Management**: Document upload and sharing
- **Time Tracking**: Task time logging and reporting
- **Notification System**: Real-time updates and alerts

### Technologies Used
- **Python 3.8+**
- **Flask**: Web framework and API development
- **SQLite**: Database for project and task storage
- **HTML5/CSS3**: Modern responsive frontend
- **JavaScript**: Interactive user interface
- **Bootstrap**: UI framework and components

### Installation

1. Clone the repository:
```bash
git clone https://github.com/galafis/Project-Management-Tool.git
cd Project-Management-Tool
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python project_manager.py
```

4. Open your browser to `http://localhost:5000`

### Usage

#### Web Interface
1. **Create Project**: Set up new projects with details and deadlines
2. **Add Tasks**: Create tasks with priorities, assignments, and due dates
3. **Manage Team**: Add team members and assign roles
4. **Track Progress**: Monitor project completion and milestones
5. **View Analytics**: Access project performance dashboards

#### API Endpoints

**Create Project**
```bash
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -d '{"name": "Website Redesign", "description": "Complete website overhaul", "deadline": "2024-12-31"}'
```

**Add Task**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"project_id": 1, "title": "Design Homepage", "priority": "high", "assigned_to": "john@example.com"}'
```

**Get Project Status**
```bash
curl -X GET http://localhost:5000/api/projects/1/status
```

#### Python API
```python
from project_manager import ProjectManager

# Initialize project manager
pm = ProjectManager()

# Create new project
project = pm.create_project(
    name="Mobile App Development",
    description="iOS and Android app development",
    deadline="2024-06-30"
)

# Add tasks
task = pm.add_task(
    project_id=project.id,
    title="UI/UX Design",
    description="Create app wireframes and designs",
    priority="high",
    assigned_to="designer@company.com"
)

# Track progress
progress = pm.get_project_progress(project.id)
print(f"Project completion: {progress['completion_percentage']}%")
```

### Project Management Features

#### Project Creation
- **Project Details**: Name, description, objectives, deadlines
- **Project Templates**: Pre-configured project types
- **Budget Tracking**: Cost estimation and expense monitoring
- **Milestone Planning**: Key project milestones and deliverables

#### Task Management
- **Task Creation**: Detailed task descriptions and requirements
- **Priority Levels**: High, medium, low priority classification
- **Task Dependencies**: Sequential task relationships
- **Subtasks**: Break down complex tasks into smaller units

#### Team Collaboration
- **User Roles**: Admin, project manager, team member, viewer
- **Task Assignment**: Assign tasks to specific team members
- **Comments**: Task-level discussion and updates
- **File Sharing**: Document and resource sharing

#### Progress Tracking
- **Completion Status**: Track task and project completion
- **Time Tracking**: Log time spent on tasks
- **Progress Reports**: Automated progress reporting
- **Gantt Charts**: Visual project timeline representation

### Dashboard Features

#### Project Overview
- **Active Projects**: Current project status and health
- **Task Summary**: Pending, in-progress, completed tasks
- **Team Workload**: Individual team member task distribution
- **Upcoming Deadlines**: Critical deadline notifications

#### Analytics
- **Performance Metrics**: Project completion rates and efficiency
- **Time Analysis**: Time spent analysis and optimization
- **Resource Utilization**: Team capacity and allocation
- **Trend Analysis**: Project performance trends over time

### Notification System

#### Real-Time Alerts
- **Task Assignments**: New task assignment notifications
- **Deadline Reminders**: Upcoming deadline alerts
- **Status Updates**: Task completion and project updates
- **Comment Notifications**: New comments and discussions

#### Email Notifications
- **Daily Summaries**: Daily task and project summaries
- **Weekly Reports**: Weekly progress reports
- **Milestone Alerts**: Milestone completion notifications
- **Overdue Alerts**: Overdue task and project notifications

### Reporting

#### Project Reports
- **Status Reports**: Current project status and progress
- **Time Reports**: Time tracking and productivity analysis
- **Budget Reports**: Cost tracking and budget analysis
- **Team Reports**: Individual and team performance metrics

#### Export Options
- **PDF Reports**: Professional project reports
- **CSV Exports**: Data export for external analysis
- **Excel Integration**: Spreadsheet-compatible exports
- **API Access**: Programmatic report generation

### Configuration
Configure project settings in `config.json`:
```json
{
  "project_settings": {
    "default_priority": "medium",
    "auto_notifications": true,
    "time_tracking": true,
    "file_upload_limit": "10MB"
  },
  "email_settings": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "daily_reports": true
  },
  "security": {
    "session_timeout": 3600,
    "password_requirements": true
  }
}
```

### Security Features
- **User Authentication**: Secure login and session management
- **Role-Based Access**: Granular permission control
- **Data Encryption**: Sensitive data protection
- **Audit Logging**: Track user actions and changes

### Integration
- **Calendar Integration**: Sync with Google Calendar, Outlook
- **File Storage**: Integration with cloud storage services
- **Communication Tools**: Slack, Microsoft Teams integration
- **Time Tracking**: Integration with time tracking tools

### Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Português

### Visão Geral
Ferramenta abrangente de gerenciamento de projetos construída com Python e Flask. Apresenta criação de projetos, gerenciamento de tarefas, colaboração em equipe, rastreamento de progresso e dashboard de analytics. Projetada para planejamento e execução eficientes de projetos com interface web moderna.

### Funcionalidades
- **Gerenciamento de Projetos**: Criar e gerenciar múltiplos projetos
- **Rastreamento de Tarefas**: Criação e atribuição abrangente de tarefas
- **Colaboração em Equipe**: Gerenciamento de usuários e acesso baseado em funções
- **Monitoramento de Progresso**: Rastreamento de progresso de projeto em tempo real
- **Dashboard Analytics**: Insights de projeto e métricas de performance
- **Gerenciamento de Arquivos**: Upload e compartilhamento de documentos
- **Rastreamento de Tempo**: Log de tempo de tarefas e relatórios
- **Sistema de Notificações**: Atualizações e alertas em tempo real

### Tecnologias Utilizadas
- **Python 3.8+**
- **Flask**: Framework web e desenvolvimento de API
- **SQLite**: Banco de dados para armazenamento de projetos e tarefas
- **HTML5/CSS3**: Frontend responsivo moderno
- **JavaScript**: Interface de usuário interativa
- **Bootstrap**: Framework UI e componentes

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/galafis/Project-Management-Tool.git
cd Project-Management-Tool
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python project_manager.py
```

4. Abra seu navegador em `http://localhost:5000`

### Uso

#### Interface Web
1. **Criar Projeto**: Configurar novos projetos com detalhes e prazos
2. **Adicionar Tarefas**: Criar tarefas com prioridades, atribuições e datas de vencimento
3. **Gerenciar Equipe**: Adicionar membros da equipe e atribuir funções
4. **Rastrear Progresso**: Monitorar conclusão de projetos e marcos
5. **Ver Analytics**: Acessar dashboards de performance de projetos

#### Endpoints da API

**Criar Projeto**
```bash
curl -X POST http://localhost:5000/api/projects \
  -H "Content-Type: application/json" \
  -d '{"name": "Redesign do Website", "description": "Reformulação completa do website", "deadline": "2024-12-31"}'
```

**Adicionar Tarefa**
```bash
curl -X POST http://localhost:5000/api/tasks \
  -H "Content-Type: application/json" \
  -d '{"project_id": 1, "title": "Design da Homepage", "priority": "high", "assigned_to": "joao@exemplo.com"}'
```

**Obter Status do Projeto**
```bash
curl -X GET http://localhost:5000/api/projects/1/status
```

#### API Python
```python
from project_manager import ProjectManager

# Inicializar gerenciador de projetos
pm = ProjectManager()

# Criar novo projeto
project = pm.create_project(
    name="Desenvolvimento de App Mobile",
    description="Desenvolvimento de app iOS e Android",
    deadline="2024-06-30"
)

# Adicionar tarefas
task = pm.add_task(
    project_id=project.id,
    title="Design UI/UX",
    description="Criar wireframes e designs do app",
    priority="high",
    assigned_to="designer@empresa.com"
)

# Rastrear progresso
progress = pm.get_project_progress(project.id)
print(f"Conclusão do projeto: {progress['completion_percentage']}%")
```

### Funcionalidades de Gerenciamento de Projetos

#### Criação de Projetos
- **Detalhes do Projeto**: Nome, descrição, objetivos, prazos
- **Templates de Projeto**: Tipos de projeto pré-configurados
- **Rastreamento de Orçamento**: Estimativa de custos e monitoramento de despesas
- **Planejamento de Marcos**: Marcos-chave do projeto e entregáveis

#### Gerenciamento de Tarefas
- **Criação de Tarefas**: Descrições detalhadas de tarefas e requisitos
- **Níveis de Prioridade**: Classificação de prioridade alta, média, baixa
- **Dependências de Tarefas**: Relacionamentos sequenciais de tarefas
- **Subtarefas**: Dividir tarefas complexas em unidades menores

#### Colaboração em Equipe
- **Funções de Usuário**: Admin, gerente de projeto, membro da equipe, visualizador
- **Atribuição de Tarefas**: Atribuir tarefas a membros específicos da equipe
- **Comentários**: Discussão e atualizações no nível da tarefa
- **Compartilhamento de Arquivos**: Compartilhamento de documentos e recursos

#### Rastreamento de Progresso
- **Status de Conclusão**: Rastrear conclusão de tarefas e projetos
- **Rastreamento de Tempo**: Registrar tempo gasto em tarefas
- **Relatórios de Progresso**: Relatórios automatizados de progresso
- **Gráficos de Gantt**: Representação visual da linha do tempo do projeto

### Funcionalidades do Dashboard

#### Visão Geral do Projeto
- **Projetos Ativos**: Status atual e saúde do projeto
- **Resumo de Tarefas**: Tarefas pendentes, em andamento, concluídas
- **Carga de Trabalho da Equipe**: Distribuição de tarefas de membros individuais
- **Prazos Próximos**: Notificações de prazos críticos

#### Analytics
- **Métricas de Performance**: Taxas de conclusão e eficiência de projetos
- **Análise de Tempo**: Análise de tempo gasto e otimização
- **Utilização de Recursos**: Capacidade e alocação da equipe
- **Análise de Tendências**: Tendências de performance de projetos ao longo do tempo

### Sistema de Notificações

#### Alertas em Tempo Real
- **Atribuições de Tarefas**: Notificações de nova atribuição de tarefa
- **Lembretes de Prazo**: Alertas de prazos próximos
- **Atualizações de Status**: Conclusão de tarefas e atualizações de projetos
- **Notificações de Comentários**: Novos comentários e discussões

#### Notificações por Email
- **Resumos Diários**: Resumos diários de tarefas e projetos
- **Relatórios Semanais**: Relatórios semanais de progresso
- **Alertas de Marcos**: Notificações de conclusão de marcos
- **Alertas de Atraso**: Notificações de tarefas e projetos atrasados

### Relatórios

#### Relatórios de Projeto
- **Relatórios de Status**: Status atual e progresso do projeto
- **Relatórios de Tempo**: Análise de rastreamento de tempo e produtividade
- **Relatórios de Orçamento**: Rastreamento de custos e análise de orçamento
- **Relatórios de Equipe**: Métricas de performance individual e da equipe

#### Opções de Exportação
- **Relatórios PDF**: Relatórios profissionais de projeto
- **Exportações CSV**: Exportação de dados para análise externa
- **Integração Excel**: Exportações compatíveis com planilhas
- **Acesso API**: Geração programática de relatórios

### Configuração
Configure as configurações do projeto em `config.json`:
```json
{
  "project_settings": {
    "default_priority": "medium",
    "auto_notifications": true,
    "time_tracking": true,
    "file_upload_limit": "10MB"
  },
  "email_settings": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "daily_reports": true
  },
  "security": {
    "session_timeout": 3600,
    "password_requirements": true
  }
}
```

### Funcionalidades de Segurança
- **Autenticação de Usuário**: Login seguro e gerenciamento de sessão
- **Acesso Baseado em Funções**: Controle granular de permissões
- **Criptografia de Dados**: Proteção de dados sensíveis
- **Log de Auditoria**: Rastrear ações e mudanças do usuário

### Integração
- **Integração de Calendário**: Sincronizar com Google Calendar, Outlook
- **Armazenamento de Arquivos**: Integração com serviços de armazenamento em nuvem
- **Ferramentas de Comunicação**: Integração Slack, Microsoft Teams
- **Rastreamento de Tempo**: Integração com ferramentas de rastreamento de tempo

### Contribuindo
1. Faça um fork do repositório
2. Crie uma branch de feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adicionar nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Crie um Pull Request

### Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

