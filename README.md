# AWS Cross-Account CI/CD Pipeline
- This project provides an AWS SAM-based solution for deploying a cross-account CI/CD pipeline using AWS CodePipeline and CodeBuild. 
- The pipeline is designed to deploy resources into both development (DEV) and production (PROD) AWS accounts, following best practices for security and automation.
- The pipeline is activated at each commit in the selected branch
- See `pipeline-structure.png` for a visual representation of the pipeline structure.

  ![pipeline-structure](https://github.com/user-attachments/assets/e712eadc-00d0-430e-81f9-be26576f61ca)


## Features

- **Cross-Account Deployment:** Uses IAM roles and trust relationships to enable secure deployments across multiple AWS accounts.
- **Automated Build & Deploy:** Leverages AWS CodeBuild and CodePipeline for automated build and deployment processes.
- **Environment Separation:** Supports separate configurations for DEV and PROD environments.
- **Infrastructure as Code:** All resources are defined using AWS SAM/CloudFormation templates.
- **Security Tools:** Integrates static analysis tools like Bandit and cfn-lint for code and template validation.

## Structure

- `pipeline/templates/pip_template.yaml`: Main pipeline CloudFormation template.
- `pipeline/templates/bootstrap_accounts.yaml`: Bootstraps target accounts with required roles and buckets.
- `samconfig.toml`: Environment-specific deployment parameters.
- `.vscode/tasks.json`: VS Code tasks for building and deploying the pipeline and bootstrap resources.
- `tools/delete_old_stack.py`: Utility script to clean up old CloudFormation stacks.

## Usage

### Prerequisites

- AWS CLI and SAM CLI installed.
- Proper AWS credentials and profiles configured for each account.
- Permissions to assume deployment roles in target accounts.

### Deployment Steps

1. **Bootstrap Target Accounts:**
   - Deploy the bootstrap template to each target account (DEV/PROD) to create artifact buckets and IAM roles.
   - Use the provided VS Code tasks:  
     - `Bootstrap DEV`
     - `Bootstrap PROD`

2. **Deploy the Pipeline:**
   - Deploy the main pipeline stack from the pipeline account.
   - Use the VS Code task:  
     - `Build & Deploy Pipeline RES`

3. **Pipeline Execution:**
   - The pipeline will automatically build and deploy resources to the configured target accounts.

### Cleaning Up
- Use `tools/delete_old_stack.py` to remove old or unused CloudFormation stacks with a specific prefix.

## Notes
- Update `samconfig.toml` and environment variables as needed for your AWS accounts and resources.

## Security
- The pipeline integrates Bandit (Python security linter) and cfn-lint (CloudFormation template linter) for enhanced security and compliance.
- All cross-account actions are performed using least-privilege IAM roles.

## License
- This project was written in 2024 for demonstration purposes only and is not intended for production use. 
- It is NOT updated regularly to reflect best practices and AWS service updates. 



