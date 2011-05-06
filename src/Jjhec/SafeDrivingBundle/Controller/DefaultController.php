<?php

namespace Jjhec\SafeDrivingBundle\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\Controller;

class DefaultController extends Controller
{
    public function indexAction()
    {
        return $this->render('JjhecSafeDrivingBundle:Default:index.html.twig',array("text"=>"value"));
    }
}
