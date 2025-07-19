"""Basic tests for spreadsheet-to-cpplib functionality."""

import pytest
import os
import tempfile
from unittest.mock import patch, MagicMock

# Import from the new location
try:
    from src.spreadsheet_to_cpplib import main
except ImportError:
    # Fallback for development
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
    from spreadsheet_to_cpplib import main


class TestBasicFunctionality:
    """Test basic functionality of the tool."""
    
    def test_main_function_exists(self):
        """Test that main function exists and is callable."""
        assert hasattr(main, 'main')
        assert callable(main.main)
    
    def test_import_structure(self):
        """Test that the package structure is correct."""
        try:
            from src.spreadsheet_to_cpplib import asciitext
            from src.spreadsheet_to_cpplib import run
            assert True
        except ImportError as e:
            pytest.fail(f"Import failed: {e}")
    
    @patch('src.spreadsheet_to_cpplib.asciitext.printText')
    @patch('src.spreadsheet_to_cpplib.run.run_cli_interface')
    def test_main_execution(self, mock_cli, mock_print):
        """Test main function execution."""
        main.main()
        mock_print.assert_called_once_with("SpreadSheet-to-cpplib")
        mock_cli.assert_called_once()


class TestProjectStructure:
    """Test project structure and file organization."""
    
    def test_required_files_exist(self):
        """Test that required project files exist."""
        project_root = os.path.dirname(os.path.dirname(__file__))
        
        required_files = [
            'README.md',
            'LICENSE',
            'pyproject.toml',
            'setup.py',
            'CONTRIBUTING.md',
            'CODE_OF_CONDUCT.md'
        ]
        
        for file_name in required_files:
            file_path = os.path.join(project_root, file_name)
            assert os.path.exists(file_path), f"Required file {file_name} not found"
    
    def test_src_directory_structure(self):
        """Test src directory structure."""
        project_root = os.path.dirname(os.path.dirname(__file__))
        src_dir = os.path.join(project_root, 'src', 'spreadsheet_to_cpplib')
        
        assert os.path.exists(src_dir), "src/spreadsheet_to_cpplib directory not found"
        
        expected_files = [
            '__init__.py',
            'main.py',
            'run.py',
            'parse.py',
            'csvToCpp.py'
        ]
        
        for file_name in expected_files:
            file_path = os.path.join(src_dir, file_name)
            assert os.path.exists(file_path), f"Source file {file_name} not found"
    
    def test_documentation_exists(self):
        """Test that documentation files exist."""
        project_root = os.path.dirname(os.path.dirname(__file__))
        docs_dir = os.path.join(project_root, 'docs')
        
        assert os.path.exists(docs_dir), "docs directory not found"
        
        expected_docs = [
            'user-guide.md',
            'api.md'
        ]
        
        for doc_name in expected_docs:
            doc_path = os.path.join(docs_dir, doc_name)
            assert os.path.exists(doc_path), f"Documentation file {doc_name} not found"


class TestConfigurationValidation:
    """Test configuration and setup validation."""
    
    def test_pyproject_toml_structure(self):
        """Test pyproject.toml has required sections."""
        project_root = os.path.dirname(os.path.dirname(__file__))
        pyproject_path = os.path.join(project_root, 'pyproject.toml')
        
        with open(pyproject_path, 'r') as f:
            content = f.read()
        
        required_sections = [
            '[build-system]',
            '[project]',
            '[project.scripts]',
            '[tool.setuptools.packages.find]'
        ]
        
        for section in required_sections:
            assert section in content, f"Required section {section} not found in pyproject.toml"
    
    def test_setup_py_compatibility(self):
        """Test setup.py exists for backward compatibility."""
        project_root = os.path.dirname(os.path.dirname(__file__))
        setup_path = os.path.join(project_root, 'setup.py')
        
        assert os.path.exists(setup_path), "setup.py not found"
        
        with open(setup_path, 'r') as f:
            content = f.read()
        
        # Check for updated import path
        assert 'src.spreadsheet_to_cpplib.main:main' in content


if __name__ == '__main__':
    pytest.main([__file__])