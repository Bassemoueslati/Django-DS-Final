from colour import Color
import sass
from celery import shared_task
from django.conf import settings
import os

@shared_task(bind=True)
def compile_scss(self, input_path=None, output_path=None):
    """Compile SCSS to CSS with proper path handling"""
    try:
        # Set default paths if not provided
        if not input_path:
            input_path = os.path.join(settings.BASE_DIR, 'static/admin/css.scss')
        if not output_path:
            output_path = os.path.join(settings.BASE_DIR, 'staticfiles/admin/compiled.css')
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Compile SCSS
        css = sass.compile(filename=input_path)
        
        # Write output
        with open(output_path, 'w') as f:
            f.write(css)
            
        return {
            'status': 'success',
            'input': input_path,
            'output': output_path,
            'message': 'SCSS compiled successfully'
        }
    except Exception as e:
        return {
            'status': 'error',
            'error': str(e),
            'input': input_path,
            'output': output_path
        }

@shared_task
def check_color_contrast(color1, color2):
    """Check WCAG color contrast ratio"""
    try:
        c1 = Color(color1)
        c2 = Color(color2)
        l1 = c1.luminance
        l2 = c2.luminance
        contrast_ratio = (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)
        
        return {
            'color1': color1,
            'color2': color2,
            'contrast_ratio': round(contrast_ratio, 2),
            'wcag_aa': contrast_ratio >= 4.5,
            'wcag_aaa': contrast_ratio >= 7,
            'luminance1': round(l1, 3),
            'luminance2': round(l2, 3)
        }
    except Exception as e:
        return {
            'error': str(e),
            'color1': color1,
            'color2': color2
        }